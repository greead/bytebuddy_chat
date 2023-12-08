<script> // Room button Svelte component
    import { onMount } from "svelte";
    import { uri, uri_ide, wss_ide, wss, current_room, message_list, ide_contents, ide_state } from "../store";
    import { get } from "svelte/store";

    export let roomName = "Room";

    // On mounting the rooms for the first time, try to connect to the "Home" room.
    onMount(() => {
        if (roomName === "Home") {
            connectRoom()
        }
    })

    /**
     * Event handler onClick for the given room component.
     * Connect to the websockets for the messages and IDEs.
     */
    async function connectRoom() {
        message_list.set([])
        ide_state.set('')

        if (get($wss).isConnected){
            $wss.disconnectWebSocket()
        }

        if (get($wss_ide).isConnected){
            $wss_ide.disconnectWebSocket()
        }

        uri.set(`ws://localhost:8000/ws/chat/${roomName.replaceAll(' ', '')}/`)
        uri_ide.set(`ws://localhost:8000/ws/ide/${roomName.replaceAll(' ', '')}/`)

        current_room.set(`${roomName}`)
        
        $wss.connectWebSocket()
        $wss_ide.connectWebSocket()
    }

</script>

<!-- Room button contents -->
<div>
    <button on:click={connectRoom}>{roomName}</button>
</div>

<style>
    div {
        display: grid;
        padding-top: 0.5em;
        padding-bottom: 0.5em;
    }
</style>