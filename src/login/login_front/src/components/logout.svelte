<script>
    import {Link, navigate} from 'svelte-routing';
    import {sessionid} from "./store.js";
    import { getCookie } from 'svelte-cookie'
    import { get } from 'svelte/store';
    let loginError = null

    async function handleLogout(event) {
        console.log(getCookie('sessionid'))
        console.log(getCookie('csrftoken'))
        console.log(getCookie('X-CSRFToken'))
        // console.log(csrf)
        try {
            const reponse = await fetch('http://127.0.0.1:8000/api/logout', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    // 'X-CSRFToken': csrf,
                },
                body: JSON.stringify({
                    "sessionid": getCookie('sessionid')
                }),
                credentials: 'include'
            });
            if(reponse.ok) {
                loginError=null
                console.log('Log out succesfully');
                navigate("/")
            } else {
                const error = await reponse.json();
                console.error(error);
                loginError = error['non_field_errors'][0];
            }
        } catch(error){
            console.error(error);
        }
    }
</script>

<div>
    <button on:click={handleLogout}>Logout</button>
</div>


<style>

</style>
