def simple_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        print(request)

        response = get_response(request)

        print(response)

        return response

    return middleware