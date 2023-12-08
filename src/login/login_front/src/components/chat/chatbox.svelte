<script> // Chatbox Svelte component
    import { onDestroy, onMount } from "svelte";
    import { uri, wss, message_list } from "../store";
    import Message from "./message.svelte";

    let messageArea;

    /**
     * Function that scrolls the message area to the bottom.
     */
    function scrollMessageAreaToBottom() {
        if (messageArea) {
        messageArea.scrollTo({
            top: messageArea.scrollHeight,
            behavior: 'smooth',
        });
        }
    } 

    /**
     * Event handler for pressing the Enter key to send a message.
     * @param event The event caller.
     */
    function handleEnterPressed(event) {
        if ((event.key) === 'Enter') {
            handleMessage();            
        }
    }

    let inputMessage = ""

    // Scroll to the bottom of the chat when the component is mounted.
    onMount(() => {
        scrollMessageAreaToBottom()
    })

    // Disconnect from the chat consumer when leaving the chat page.
    onDestroy(() => {
        $wss.disconnectWebSocket()
    })

    // Subscribe to the chat consumer store (observer).
    // Update the message list with the new messages when a new message is received.
    $wss.subscribe((store) => {
        console.log("msg in sub", store.message)
        message_list.update((values) => ([...values, store.message]))
    })

    /**
     * Event handler for sending a message. Scrolls to the bottom of the chatbox.
     * @param event The event caller.
     */
    async function handleMessage(event) {
        await $wss.sendMessage(inputMessage)        
        scrollMessageAreaToBottom()
        inputMessage = ''
    }

</script>

<!-- Chatbox contents -->
<div class="chatbox">
    <div id="messageArea" class="messageArea">        
        <ul role="listbox" bind:this={messageArea}>
            {#each $message_list as message, i}
                <li class:even={i % 2 === 0} class:odd={i % 2 !== 0}><Message user={message.user} message={message.content} system={message.sys}/></li>
            {/each}
        </ul>
    </div>
    
    <div id="messageBox" class="messageBox">
        <input bind:value={inputMessage} type="text" id="textBox" name="textBox" class="textBox" on:keypress={handleEnterPressed} autocomplete="off">
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