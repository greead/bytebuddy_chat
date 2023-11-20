<script>
    import { uri, wss } from "../store";
    import { get } from "svelte/store";

    export let roomName = "Room";

    async function connectRoom() {
        if (get($wss).isConnected){
            $wss.disconnectWebSocket()
        }
        // TODO set WebSocket uri based on the ChatConsumer's syntax
        uri.set('ws://localhost:8000/ws/chat/default/') // <-- Placeholder
        $wss.connectWebSocket()
    }

</script>

<div>
    <button on:click={connectRoom} >{roomName}</button>
</div>

<style>
    div {
        display: grid;
        padding-top: 0.5em;
        padding-bottom: 0.5em;
    }
</style>