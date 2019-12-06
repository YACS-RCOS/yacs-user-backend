# Yacs User Backend Service API Document

## /users
<details>
    <summary>GET</summary>
    Get the users information.
    <details>
        <summary>Request</summary>
        ```json
        {
            "sessionID" : "43243-4324-324-234-32"
        }
        ```
    </details>
    <details>
        <summary>Response</summary>
        ```json
        {
        success: true,
        errMsg: null, 
        content:
            {
                "uid": "4",
                "name": "John",
                "email": "aaa@wa.com",
                "phone": "51829838475",
                "major": "CS",
                "degree": "Undergraduate"
            }
        }
        ```
    </details>
</details>

