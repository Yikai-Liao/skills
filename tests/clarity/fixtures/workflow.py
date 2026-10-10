"""Services record their calls; all three checks can have side effects."""


def submit(request, service):
    if service.authenticated(request):
        if service.has_quota(request):
            if service.valid_input(request):
                result = service.commit(request)
                return result
            else:
                raise ValueError("invalid input")
        else:
            raise RuntimeError("quota exceeded")
    else:
        raise PermissionError("unauthorized")
