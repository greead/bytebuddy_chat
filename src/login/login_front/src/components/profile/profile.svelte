<script>
    import Nav from "../navbar/nav.svelte"
    import {displayName, bio,userid, csrf} from "../store"
    console.log($userid)
    import { onMount } from 'svelte';

    onMount(() => {
        getPfp()
    });

    // To-do:
    // views and urls are alreaday set up to return a url in json format
    // need to figure out a way to send post request to backend server
    // right now, if I refresh page, userID, sessionID and CSRF are also reset
    // so, I couldn't use them. Also, since we have sessionID, should we use it instead of CSRF
    async function getPfp(event) {
        let res = await fetch("http://localhost:8000/profilePicture/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": $csrf,
            },
            credentials: "include",
            body: JSON.stringify({userid: $userid}),
    })

        let dat = await res.json()
        console.log(dat)
    }
</script>

<Nav />

<!-- To-do: need to add a box for profile picture and position things around -->
<div id= "flex">
    <div class="idky">
        <lable for="displayName">DisplayName </lable>
        <input bind:value={$displayName} type="text" id="displayName" name="displayName" style="input_item">
    </div>
    <div class="idky">
        <lable for="bio">Bio</lable>
        <textarea bind:value={$bio} id="bio" name="bio"></textarea>
    </div>
</div>