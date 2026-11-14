// Compatibility replacement for boost::beast::handler_ptr, which was removed from Boost.Beast
// (deprecated in Boost 1.70, removed in 1.85). The Thymio Device Manager's hand-written
// asynchronous operations still use it. Same semantics as the original: owns the completion
// handler and a state object; invoke() destroys the state, then calls the handler.
//
// Copyright 2026 Mobsya / Thymio Suite Next contributors. Distributed under the
// Boost Software License, Version 1.0 (same as the original Beast class).
#pragma once
#include <memory>
#include <utility>

namespace boost {
namespace beast {

template <class T, class Handler>
class handler_ptr {
    struct holder {
        Handler handler;
        T state;
        template <class DeducedHandler, class... Args>
        explicit holder(DeducedHandler&& h, Args&&... args)
            : handler(std::forward<DeducedHandler>(h)), state(handler, std::forward<Args>(args)...) {}
    };
    std::unique_ptr<holder> p_;

public:
    using element_type = T;
    using handler_type = Handler;

    handler_ptr(handler_ptr&&) = default;
    handler_ptr(handler_ptr const&) = delete;
    handler_ptr& operator=(handler_ptr&&) = delete;
    handler_ptr& operator=(handler_ptr const&) = delete;

    template <class DeducedHandler, class... Args>
    explicit handler_ptr(DeducedHandler&& handler, Args&&... args)
        : p_(std::make_unique<holder>(std::forward<DeducedHandler>(handler), std::forward<Args>(args)...)) {}

    bool has_value() const noexcept {
        return p_ != nullptr;
    }
    handler_type const& handler() const noexcept {
        return p_->handler;
    }
    handler_type& handler() noexcept {
        return p_->handler;
    }
    T* get() const noexcept {
        return p_ ? &p_->state : nullptr;
    }
    T& operator*() const noexcept {
        return p_->state;
    }
    T* operator->() const noexcept {
        return &p_->state;
    }

    handler_type release_handler() {
        handler_type h(std::move(p_->handler));
        p_.reset();
        return h;
    }

    template <class... Args>
    void invoke(Args&&... args) {
        handler_type h(std::move(p_->handler));
        p_.reset();
        h(std::forward<Args>(args)...);
    }
};

}  // namespace beast
}  // namespace boost
