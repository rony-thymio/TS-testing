# Standalone build of the Thymio Device Manager (TDM) from the Mobsya/aseba source tree.
#
# Why: the original aseba build requires Qt 5 even for the device manager, pins Boost 1.78 and
# OpenSSL 1.0.2, and no longer builds on current macOS. This file builds only the device manager
# and the firmware upgrader, with no Qt, a current Boost (fetched automatically) and OpenSSL 3.
#
#   cmake -S device-manager -B build -G Ninja -DASEBA_SOURCE_DIR=/path/to/aseba
#   cmake --build build
cmake_minimum_required(VERSION 3.24)
project(thymio-device-manager-next LANGUAGES C CXX)

set(ASEBA_SOURCE_DIR "" CACHE PATH "Path to a checkout of github.com/Mobsya/aseba (with submodules)")
if(NOT EXISTS "${ASEBA_SOURCE_DIR}/aseba/thymio-device-manager/main.cpp")
    message(FATAL_ERROR "Set ASEBA_SOURCE_DIR to a Mobsya/aseba checkout (got '${ASEBA_SOURCE_DIR}')")
endif()
set(A "${ASEBA_SOURCE_DIR}")
set(TDM "${A}/aseba/thymio-device-manager")

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_POSITION_INDEPENDENT_CODE ON)
set(BUILD_SHARED_LIBS OFF)
if(WIN32)
    # Keep <windows.h> from pulling in the old <winsock.h>, which conflicts with Boost.Asio.
    add_compile_definitions(WIN32_LEAN_AND_MEAN NOMINMAX _WIN32_WINNT=0x0A00)
endif()
if(MSVC)
    add_compile_options(/utf-8 /permissive- /bigobj)
    # Static runtime: a single .exe with no Visual C++ redistributable needed in schools.
    set(CMAKE_MSVC_RUNTIME_LIBRARY "MultiThreaded$<$<CONFIG:Debug>:Debug>")
endif()
if(CMAKE_CXX_COMPILER_ID STREQUAL "GNU")
    # The bundled range-v3 (2018) trips a GCC 13 check; harmless.
    add_compile_options($<$<COMPILE_LANGUAGE:CXX>:-Wno-changes-meaning>)
endif()
if(APPLE)
    set(CMAKE_OSX_DEPLOYMENT_TARGET "11.0" CACHE STRING "Minimum macOS version")
endif()
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/bin")

find_package(Threads REQUIRED)

# These change the layout of Boost.Asio types, so they must be identical for every library
# linked into the device manager (aware, belle, the TDM itself). Setting them only on the TDM
# target made aware's sockets a different size and crashed at start-up on macOS.
add_compile_definitions(
    BOOST_ALLOW_DEPRECATED_HEADERS
    BOOST_THREAD_PROVIDES_FUTURE_CONTINUATION
    BOOST_BEAST_ALLOW_DEPRECATED
    BOOST_ASIO_USE_TS_EXECUTOR_AS_DEFAULT   # pre-1.74 executor model the code was written for
    $<$<BOOL:${WIN32}>:BOOST_USE_WINDOWS_H>)

# Workarounds for old bundled headers with current compilers (see compat/force_include.h).
if(MSVC)
    add_compile_options("$<$<COMPILE_LANGUAGE:CXX>:/FI${CMAKE_CURRENT_SOURCE_DIR}/compat/force_include.h>")
else()
    add_compile_options("$<$<COMPILE_LANGUAGE:CXX>:SHELL:-include ${CMAKE_CURRENT_SOURCE_DIR}/compat/force_include.h>")
endif()

# ---------------------------------------------------------------- Boost (current, fetched)
set(TDM_BOOST_VERSION "1.86.0" CACHE STRING "Boost release to use")
include(FetchContent)
set(BOOST_INCLUDE_LIBRARIES asio beast program_options filesystem date_time thread uuid
    signals2 scope_exit interprocess chrono regex system multiprecision endian)
set(BOOST_ENABLE_CMAKE ON)
FetchContent_Declare(Boost
    URL "https://github.com/boostorg/boost/releases/download/boost-${TDM_BOOST_VERSION}/boost-${TDM_BOOST_VERSION}-cmake.tar.xz"
    DOWNLOAD_EXTRACT_TIMESTAMP ON
    EXCLUDE_FROM_ALL)
FetchContent_MakeAvailable(Boost)

# ---------------------------------------------------------------- OpenSSL 3 (system)
if(APPLE OR WIN32)
    set(OPENSSL_USE_STATIC_LIBS TRUE)
    if(WIN32)
        set(OPENSSL_MSVC_STATIC_RT TRUE)
    endif()
endif()
find_package(OpenSSL 3 REQUIRED)

# ---------------------------------------------------------------- Zeroconf (Bonjour / DNS-SD)
# Used to advertise the TDM so Thonny/tdmclient and other computers can find it.
add_library(zeroconf INTERFACE)
set(TDM_ZEROCONF_LINKED ON)
if(WIN32)
    target_include_directories(zeroconf INTERFACE "${A}/third_party/bonjour/include")
    target_link_libraries(zeroconf INTERFACE "${A}/third_party/bonjour/lib/x64/dnssd64.lib" ws2_32)
elseif(APPLE)
    # dns_sd is part of libSystem on macOS.
else()
    find_path(DNSSD_INCLUDE_DIR dns_sd.h)
    find_library(DNSSD_LIBRARY dns_sd)
    if(DNSSD_INCLUDE_DIR AND DNSSD_LIBRARY)
        target_include_directories(zeroconf INTERFACE "${DNSSD_INCLUDE_DIR}")
        target_link_libraries(zeroconf INTERFACE "${DNSSD_LIBRARY}")
    else()
        # Developer machines without dns_sd: use a stub that reports "zeroconf not running".
        # Also useful to test behaviour on networks where zeroconf is blocked. Not for releases.
        message(WARNING "dns_sd not found: using dev/dnssd_stub.c (zeroconf disabled)")
        add_library(dnssd_stub STATIC "${CMAKE_CURRENT_SOURCE_DIR}/dev/dnssd_stub.c")
        target_include_directories(dnssd_stub PUBLIC "${A}/third_party/bonjour/include")
        target_link_libraries(zeroconf INTERFACE dnssd_stub)
    endif()
endif()

# ---------------------------------------------------------------- Third-party (from aseba)
add_library(spdlog INTERFACE)
target_include_directories(spdlog INTERFACE "${A}/third_party/spdlog/spdlog/include")
add_library(tl_expected INTERFACE)
target_include_directories(tl_expected INTERFACE "${A}/third_party/expected/expected/include")
add_library(mpark_variant INTERFACE)
target_include_directories(mpark_variant INTERFACE "${A}/third_party/mpark.variant/include")
add_library(range-v3 INTERFACE)
target_include_directories(range-v3 INTERFACE "${A}/third_party/range-v3/include")
add_library(fmt-header-only INTERFACE)
target_include_directories(fmt-header-only INTERFACE "${A}/third_party/fmt/include")
target_compile_definitions(fmt-header-only INTERFACE FMT_HEADER_ONLY=1)

# libusb headers are used on every platform (error codes, firmware upgrader); the library itself on Linux only.
add_library(libusb_headers INTERFACE)
target_include_directories(libusb_headers INTERFACE "${A}/third_party/libusb/libusb" "${A}/third_party/libusb/include")

add_library(pugixml STATIC "${A}/third_party/pugixml/src/pugixml.cpp")
target_include_directories(pugixml PUBLIC "${A}/third_party/pugixml/src")

# aware: zeroconf announce/browse on top of Boost.Asio (Bonjour backend)
file(GLOB AWARE_BONJOUR_SRC "${A}/third_party/aware/src/bonjour/*.cpp" "${A}/third_party/aware/src/bonjour/detail/*.cpp")
add_library(aware STATIC
    ${AWARE_BONJOUR_SRC}
    "${A}/third_party/aware/src/contact.cpp"
    "${A}/third_party/aware/src/detail/native_socket.cpp"
    "${A}/third_party/aware/src/detail/utility.cpp")
target_include_directories(aware PUBLIC "${A}/third_party/aware/include")
target_compile_definitions(aware PUBLIC AWARE_HAS_BONJOUR)
target_link_libraries(aware PUBLIC Boost::asio Boost::chrono zeroconf)

# flatbuffers: build flatc for the host, then generate the protocol header
# The 2018 flatbuffers CMakeLists asks for CMake 2.8, which CMake 4 refuses without this.
set(CMAKE_POLICY_VERSION_MINIMUM 3.5)
set(FLATBUFFERS_BUILD_TESTS OFF CACHE BOOL "" FORCE)
set(FLATBUFFERS_BUILD_FLATHASH OFF CACHE BOOL "" FORCE)
set(FLATBUFFERS_INSTALL OFF CACHE BOOL "" FORCE)
add_subdirectory("${A}/third_party/flatbuffers" flatbuffers EXCLUDE_FROM_ALL)
set(FB_SCHEMA "${A}/aseba/flatbuffers/thymio.fbs")
set(FB_HEADER "${CMAKE_BINARY_DIR}/aseba/flatbuffers/thymio_generated.h")
add_custom_command(OUTPUT "${FB_HEADER}"
    COMMAND flatc --cpp --no-includes --gen-mutable --scoped-enums --gen-object-api
            --cpp-ptr-type std::unique_ptr -o "${CMAKE_BINARY_DIR}/aseba/flatbuffers" "${FB_SCHEMA}"
    DEPENDS flatc "${FB_SCHEMA}")

# ---------------------------------------------------------------- Aseba core
add_library(aseba_conf INTERFACE)
target_compile_definitions(aseba_conf INTERFACE ASEBA_ASSERT $<$<BOOL:${WIN32}>:WIN32_LEAN_AND_MEAN NOMINMAX>)
target_include_directories(aseba_conf INTERFACE "${A}/aseba" "${A}")

add_library(thymio-flatbuffers STATIC "${A}/aseba/flatbuffers/thymio-flatbuffers.cpp" "${FB_HEADER}")
target_link_libraries(thymio-flatbuffers PUBLIC flatbuffers aseba_conf)
target_include_directories(thymio-flatbuffers PUBLIC "${CMAKE_BINARY_DIR}" "${A}/third_party/flatbuffers/include")

file(READ "${A}/VERSION.txt" _ver)
string(REGEX MATCH "[0-9]+\\.[0-9]+\\.[0-9]+" ASEBA_VERSION "${_ver}")
set(GIT_REVISION "next")
configure_file("${A}/aseba/common/version.cpp.tpl" "${CMAKE_BINARY_DIR}/version.cpp")
add_library(asebacommon STATIC
    "${A}/aseba/common/utils/FormatableString.cpp"
    "${A}/aseba/common/utils/utils.cpp"
    "${A}/aseba/common/msg/msg.cpp"
    "${A}/aseba/common/msg/TargetDescription.cpp"
    "${CMAKE_BINARY_DIR}/version.cpp")
target_link_libraries(asebacommon PUBLIC aseba_conf)

file(GLOB ASEBACOMPILER_SRC "${A}/aseba/compiler/*.cpp")
add_library(asebacompiler STATIC ${ASEBACOMPILER_SRC})
target_link_libraries(asebacompiler PUBLIC asebacommon)

# ---------------------------------------------------------------- Device manager
file(GLOB TDM_COMMON_SRC "${TDM}/*.cpp")
list(FILTER TDM_COMMON_SRC EXCLUDE REGEX "(serialacceptor_|serialserver|usbserver|usbacceptor|usbdevice|thymio2_fwupgrade_standalone_main|/main\\.cpp$)")
add_library(thymio-device-manager-lib STATIC ${TDM_COMMON_SRC})

if(WIN32)
    target_sources(thymio-device-manager-lib PRIVATE "${TDM}/serialacceptor_win32.cpp" "${TDM}/serialserver.cpp")
    target_compile_definitions(thymio-device-manager-lib PUBLIC MOBSYA_TDM_ENABLE_SERIAL)
    target_link_libraries(thymio-device-manager-lib PUBLIC iphlpapi crypt32 bcrypt winspool ws2_32 setupapi)
elseif(APPLE)
    target_sources(thymio-device-manager-lib PRIVATE "${TDM}/serialacceptor_osx.cpp" "${TDM}/serialserver.cpp")
    target_compile_definitions(thymio-device-manager-lib PUBLIC MOBSYA_TDM_ENABLE_SERIAL)
    target_link_libraries(thymio-device-manager-lib PUBLIC "-framework CoreFoundation" "-framework IOKit")
else()
    # Linux: libusb backend, as in the original build when udev is not used.
    set(LIBUSB "${A}/third_party/libusb/libusb/libusb")
    add_library(libusb STATIC "${LIBUSB}/core.c" "${LIBUSB}/descriptor.c" "${LIBUSB}/hotplug.c"
        "${LIBUSB}/io.c" "${LIBUSB}/sync.c" "${LIBUSB}/strerror.c"
        "${LIBUSB}/os/poll_posix.c" "${LIBUSB}/os/threads_posix.c"
        "${LIBUSB}/os/linux_usbfs.c" "${LIBUSB}/os/linux_netlink.c")
    target_include_directories(libusb PUBLIC "${A}/third_party/libusb/include" "${LIBUSB}")
    target_compile_definitions(libusb PRIVATE HAVE_SYS_TIME_H HAVE_POLL_H HAVE_UNISTD_H HAVE_STRUCT_TIMESPEC
        THREADS_POSIX POLL_NFDS_TYPE=nfds_t _GNU_SOURCE OS_LINUX USBI_TIMERFD_AVAILABLE HAVE_PIPE2)
    target_link_libraries(libusb PUBLIC Threads::Threads)
    target_sources(thymio-device-manager-lib PRIVATE "${TDM}/usbserver.cpp" "${TDM}/usbacceptor.cpp" "${TDM}/usbdevice.cpp")
    target_compile_definitions(thymio-device-manager-lib PUBLIC MOBSYA_TDM_ENABLE_USB USE_MPARK)
    target_link_libraries(thymio-device-manager-lib PUBLIC libusb)
endif()

# compat/ goes first: it restores APIs that newer Boost removed (see compat/README.md).
target_include_directories(thymio-device-manager-lib BEFORE PUBLIC "${CMAKE_CURRENT_SOURCE_DIR}/compat")
target_include_directories(thymio-device-manager-lib PUBLIC "${A}/third_party/belle/include")
target_compile_definitions(thymio-device-manager-lib PUBLIC SPDLOG_FMT_EXTERNAL)
target_link_libraries(thymio-device-manager-lib PUBLIC
    asebacommon asebacompiler thymio-flatbuffers
    Boost::asio Boost::beast Boost::program_options Boost::filesystem Boost::date_time
    Boost::thread Boost::uuid Boost::multiprecision Boost::endian Boost::signals2 Boost::scope_exit Boost::interprocess
    spdlog tl_expected aware libusb_headers fmt-header-only mpark_variant pugixml range-v3
    OpenSSL::SSL OpenSSL::Crypto Threads::Threads ${CMAKE_DL_LIBS})

if(TDM_ZEROCONF_LINKED)
    add_executable(thymio-device-manager "${TDM}/main.cpp")
    target_link_libraries(thymio-device-manager PRIVATE thymio-device-manager-lib)
    add_executable(thymio2-firmware-upgrader "${TDM}/thymio2_fwupgrade_standalone_main.cpp")
    target_link_libraries(thymio2-firmware-upgrader PRIVATE thymio-device-manager-lib)
endif()

# The 2018 flatbuffers sources use -Werror; newer compilers add warnings that would fail the build.
foreach(t flatbuffers flatc)
    if(TARGET ${t} AND NOT MSVC)
        target_compile_options(${t} PRIVATE -Wno-error)
    endif()
endforeach()
