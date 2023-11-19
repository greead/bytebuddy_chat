<script>
    import { uri, wss } from "../store";
    import { get } from "svelte/store";

    export let roomName = "Room";

    async function connectRoom() {
        if (get($wss).isConnected){
            $wss.disconnectWebSocket()
        }
        // TODO set WebSocket uri based on the ChatConsumer's syntax
        uri.set('wss://socketsbay.com/wss/v2/1/demo/') // <-- Placeholder
        $wss.connectWebSocket()
    }

</script>

<div>
    <button on:click={connectRoom} >{roomName}</button>
</div>

<style>
    div {
        display: grid;
        padding-right: 4px;
        padding-bottom: 4px;
    }
</style>