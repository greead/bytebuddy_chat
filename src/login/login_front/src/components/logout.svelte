<script>
    import {Link} from 'svelte-routing';
    import {user} from "./store.js";
    let loginError = null

    async function handleLogout(event) {
        try {
            const reponse = await fetch('http://127.0.0.1:8000/api/logout', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify($user),
            });
            if(reponse.ok) {
                loginError=null
                console.log('Log out succesfully');
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

<Link to="/">
    <button on:click={handleLogout}>Logout</button>
</Link>
