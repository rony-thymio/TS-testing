# compat

Small headers that restore APIs removed from newer libraries, so the 2.4.0 device manager
code builds with current Boost without large rewrites.

- `boost/beast/core/handler_ptr.hpp`: removed from Boost.Beast in 1.85.
