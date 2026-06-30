# from playwright.sync_api import sync_playwright
# def test_delete_user():
#     with sync_playwright() as p:
#         request=p.request.new_context()
#         response=request.delete("https://jsonplaceholder.typicode.com/users/1")

#         assert response.status in [200,204]