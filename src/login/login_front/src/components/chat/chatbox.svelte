<script>
    import { onDestroy, onMount } from "svelte";
    import { uri, wss } from "../store";

    let messageArea;

    function scrollMessageAreaToBottom() {
        if (messageArea) {
        messageArea.scrollTo({
            top: messageArea.scrollHeight,
            behavior: 'smooth', // You can change this to 'auto' for instant scrolling
        });
        }
    } 

    let messageList = []
    let inputMessage = ""

    onMount(() => {
        
    })

    onDestroy(() => {
        $wss.disconnectWebSocket()
    })

    $wss.subscribe((store) => {
        console.log("msg in sub", store.message)
        messageList = [...messageList, store.message]
    })

    async function handleMessage(event) {
        await $wss.sendMessage(inputMessage)
        
        scrollMessageAreaToBottom()
        document.getElementById('textBox').value='';
    }

</script>

<div class="chatbox">
    <div id="messageArea" class="messageArea">        
        <ul role="listbox" bind:this={messageArea}>
            {#each messageList as message, i}
                <li class:even={i % 2 === 0} class:odd={i % 2 !== 0}>{message}</li>
            {/each}
        </ul>
    </div>
    
    <div id="messageBox" class="messageBox">
        <input bind:value={inputMessage} type="text" id="textBox" name="textBox" class="textBox">
        <button on:click={handleMessage} class="submit">Send</button>
    </div>
</div>


<style>
    ul {
        list-style: none;
        margin: 0;
        padding: 0;
        text-align: left;
        max-height: 100%;
        text-indent: 10px;
        overflow: auto;
        
    }

    /* chat history*/
    .messageArea {
        width: 100%;
        height: 68%;
        background-color: #0700d2;
        color: white;
        border-radius: 1em; 
        padding:1em;
        box-sizing: border-box;
    }

    /* where you type your message and button */
    .messageBox {
        display: flex;
        width:100%;
        flex-direction:row;
        /* width: 50vw; */
        align-items: center;
        justify-content: space-between;
    }

    /* where you type your message */
    input {
        box-sizing: border-box;
        height:90%;
        width: 85%;
        border-radius:0.6em;
        border-color: #ccc;
        padding: 10px; 
        font-family: 'VT323';
    }

    /* button */
    .submit {
        /* width: 20%; */
        height:100%;
        border-radius: 0.3em;
    }

    /* where you type, submit button and chat history */
    .chatbox {
        /* width: 50vw; */
        display:flex;
        flex-direction: column;
        align-items: center;
        justify-content: space-evenly;
        height: 60%;
        width: 50vw;
        font-family: 'VT323';
    }

    .even {
        background-color: rpg rd#2a2796;
    }

    .odd {
        background-color:#0500a3;
    }
</style>