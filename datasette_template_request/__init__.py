from datasette import hookimpl


@hookimpl
def extra_template_vars(request):
    return {"request": request}
