<script>
    import Logout from "../auth/logout.svelte";
    import {Link, navigate} from "svelte-routing";
</script>

<div class="topbar">
    <h3>ByteBuddy</h3>
    <div id="buttons">
        <button on:click={() => navigate("/chat")}>Chat Rooms</button>
        <button on:click={() => navigate("/profile")}>Profile</button>
        <Logout/>
    </div>
</div>

<style>
    .topbar{
        font-family: "VT323", serif;
        width:100%;
        display: flex;
        align-items: center; /* Vertical centering */
        justify-content: space-between;
        
        /* margin-right:4em; */
        /* margin-left:4em; */
    }

    h3{
        /* color:#0900ff; */
        color:white;
        font-size:1.5em;
        margin-left: 3em;
        margin-right:3em;
    }

    #buttons{
        margin-left:3em;
        margin-right:3em;
    }

    button{
        /* margin-left:1em; */
        /* margin-right:1em; */
    }
</style>