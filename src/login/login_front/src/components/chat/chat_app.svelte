<script> // Chat app Svelte component
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

    // When the component is mounted, fetch the rooms
    onMount(() => {
        getRoomsList()
    })

    /**
     * Get the list of rooms for the rooms bar.
     */
    async function getRoomsList() {
        let apiRooms = []
        // Future work: Fetch rooms from API and allow users to create and delete their own rooms.
        roomsList = ["Home", "Java Cafe", "Python Burrow", "JavaScript Torture Chamber"]
    }

</script>

<!-- Chat app content -->
<div class="system">
    <Nav/>
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
</div>



<style>
    h2{
        font-family: 'VT323';
    }

    .divchatbox{
        height:100% ;
        display: flex;
        flex-direction: column;
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
    }
   
</style>

