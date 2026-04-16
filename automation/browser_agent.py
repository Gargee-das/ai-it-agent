from playwright.sync_api import sync_playwright

def perform_action(task):
    print("Running automation:", task)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("http://localhost:8000")
        page.wait_for_timeout(2000)

        email = task["email"]

        page.fill('input[name="email"]', email)

        if task["action"] == "create_user":
            page.click('text=Create')

        elif task["action"] == "reset_password":
            page.click('text=Reset')

        elif task["action"] == "assign_license":
            page.click('text=Assign')

        page.wait_for_timeout(2000)
        browser.close()

from playwright.sync_api import sync_playwright

def perform_notion_task():
    print("Running Notion automation")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Open Notion
        page.goto("https://www.notion.so/")
        page.wait_for_timeout(8000)

        # Just click anywhere editable (safe)
        try:
            page.click("body")
        except:
            pass

        # Try typing something (safe fallback)
        try:
            page.keyboard.type("Created by AI agent 🚀")
        except:
            print("Typing failed")

        page.wait_for_timeout(3000)
        browser.close()        