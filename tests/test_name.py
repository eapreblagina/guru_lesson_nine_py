from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


def test_git_name_issue():
    browser.open('https://github.com')

    s('.header-search-button').click()
    s('#query-builder-test').set_value('eroshenkoam/allure-example')
    s('#query-builder-test').press_enter()

    s(by.link_text('eroshenkoam/allure-example')).click()
    s('#issues-tab').click()

    s(by.partial_text('#76')).should(be.visible)