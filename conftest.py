import pytest


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    if report.when == "call":
        # always add url to report    
        #extra.append(pytest_html.extras.image("/opt/app/report/ss3.png"))
        #extra.append(pytest_html.extra.image('report/ss2.png', mime_type='image/gif', extension='gif'))
        #extra.append(extra.image('report/ss1.png', mime_type='ss1.png/gif', extension='gif'))
        extra.append(pytest_html.extras.image('ss2.png'))
        extra.append(pytest_html.extras.image('ss1.png'))
        extra.append(pytest_html.extras.url('https://appliedaiconsulting.com/'))
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            # only add additional html on failure
            #extra.append(pytest_html.extras.image("/opt/app/report/ss3.png"))
            extra.append(pytest_html.extras.image("report/ss2.png"))
            extra.append(pytest_html.extras.image("report/ss1.png"))
            extra.append(pytest_html.extras.html("<div>Additional HTML</div>"))
        report.extra = extra
