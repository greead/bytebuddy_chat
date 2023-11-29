<script>
    import Logout from "../auth/logout.svelte";
    import Chatbox from "./chatbox.svelte";
    import RoomsBar from "./rooms_bar.svelte";
    import Ide from "./ide.svelte";
    import UsersBar from "./users_bar.svelte";
    import { onMount } from "svelte";
    import Nav from "../navbar/nav.svelte"
    import {userid, user_store, current_room} from "../store";
    let roomsList = []
    let profilesList = []
    console.log($userid)
    onMount(() => {
        getRoomsList()
        // getProfilesList()
    })

    async function getRoomsList() {
        let apiRooms = []
        // TODO fetch rooms from API
        roomsList = ["Home", "Java Cafe", "Python Burrow", "JavaScript Torture Chamber"] // <-- Placeholder
    }

</script>


<div class="system">
    <Nav/>
    <!-- <div class="chatbox"> -->
        <div class="main">
            <RoomsBar rooms={roomsList}/>
            <div class="divchatbox">
                <h2>{$current_room}</h2>
                {#if $current_room != "Home"}
                    <Ide/>
                {/if}
                <Chatbox/>
            </div>
            <UsersBar users={$user_store}/>
        </div>
    
    <!-- </div> -->
</div>



<style>
    .divchatbox{
        height:100%;
    }

    .system{
        display:flex;
        flex-direction: column;
        align-items: center;
        justify-content: space-between;
        width:100vw;
        height:50vw;

    }
    .main {
        width:92%;
        display: flex;
        flex-direction: row;
        align-items: start;
        justify-content: space-evenly;
        height: 100%;
        margin-top:1em;
        /* border-color: black;
        border-radius:5em;
        border: 0.1em solid #eeeeee;  */
    }
   
</style>

