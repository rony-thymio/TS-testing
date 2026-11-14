// Included at the top of every C++ file of the device manager build (see CMakeLists.txt).
// Works around old bundled third-party headers that no longer compile with current toolchains,
// without modifying them.
#pragma once

// range-v3 (2018) uses PTRDIFF_MAX/SIZE_MAX without including <cstdint>; newer GCC no longer
// includes it indirectly.
#include <cstdint>

#if defined(_MSC_VER)
// fmt 6 (2019) uses stdext::checked_array_iterator whenever _SECURE_SCL is defined. That class was
// removed from the Visual Studio 2022 standard library. _SECURE_SCL itself is a legacy macro that
// the library no longer uses, so undefine it and fmt falls back to plain pointers.
#include <yvals.h>
#undef _SECURE_SCL
#endif
