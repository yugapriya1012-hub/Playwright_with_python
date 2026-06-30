# from playwright.sync_api import sync_playwright

# def test_get_user():
#     with sync_playwright() as p:
#         request=p.request.new_context()

#         response=request.get("https://jsonplaceholder.typicode.com/users")

#         assert response.status==200

#         data=response.json()
#         print(data)

#         assert len(data)>0