<script>
    import Logout from "../auth/logout.svelte";
    import Chatbox from "./chatbox.svelte";
    import RoomsBar from "./rooms_bar.svelte";
    import Ide from "./ide.svelte";
    import UsersBar from "./users_bar.svelte";
    import { onMount } from "svelte";
    import Nav from "../navbar/nav.svelte"
    import {userid, user_store} from "../store";
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
        roomsList = ["Dummy1", "Dummy2", "Dummy 3"] // <-- Placeholder
    }

    // async function getProfilesList() {
    //     let apiProfiles = []
    //     profilesList = $user_store
    // }

</script>


<div class="system">
    <Nav/>
    <!-- <div class="chatbox"> -->
        <div class="main">
            <RoomsBar rooms={roomsList}/>
            <div class="divchatbox">
                <Ide/>
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

