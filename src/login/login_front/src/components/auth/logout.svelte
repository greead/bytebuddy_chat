<script> // Logout button Svelte component.
    import { navigate } from 'svelte-routing';

    /**
     * Event handler for logging out on button press.
     * @param event The event caller.
     */
    async function handleLogout(event) {
        let res = await fetch("http://localhost:8000/logout/", {
            credentials: "include",
        })

        if (res.ok) {
            navigate('/')
        }
    }
    
</script>

<!-- Logout button -->
<button on:click={handleLogout}>Logout</button>
