<script> // Navigation buttons svelte component
    import Logout from "../auth/logout.svelte";
    import {Link, navigate} from "svelte-routing";
</script>

<!-- Navigation buttons -->
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
        align-items: center;
        justify-content: space-between;
    }

    h3{
        color:white;
        font-size:1.5em;
        margin-left: 3em;
        margin-right:3em;
    }

    #buttons{
        margin-left:3em;
        margin-right:3em;
    }

</style>