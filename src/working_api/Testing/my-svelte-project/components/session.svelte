<script>
    import { sessionid, auth, data } from './store'

    async function handleSession(event) {
        let res = await fetch("http://localhost:8000/api/session/", {
            credentials: "include",
        })

        let dat = await res.json()

        data.set(dat.isAuthenticated)
        sessionid.set(dat.sessionid)
    }
    
</script>

<button on:click={handleSession}>Session</button>