<script>
    import {Link} from 'svelte-routing';
    // let hover = true;
    function hoverOver(event){
        event.target.style.color= "#0900ff";
        event.target.style.backgroundColor="white";
    }

    function hoverOut(event){
        event.target.style.color= "white";
        event.target.style.backgroundColor="#0900ff";
    }
</script>

<h2>Welcome to</h2>
<h1>ByteBuddy</h1>
<h3>The Retro Chatroom for Purdue Fort Wayne students! </h3>
<div id="intro"> Are you a Computer Science major, a programming enthusiast, or a casual person eager to connect with fellow students? 
    ByteBuddy offers real-time conversations with people from all corners of Purdue Fort Wayne. If you are a student programmer seeking 
    help or answers, we've got you covered as ByteBuddy provides in-chat compiler to turn your text to codes. 
    Join ChatRoomHub today and be part of the conversation.
</div>
<div  id="buttons">
    <Link to="/login">
        <button on:mouseenter={hoverOver} on:mouseleave={hoverOut}>Log In</button>
    </Link>
    <Link to="/signup">
        <button on:mouseenter={hoverOver} on:mouseleave={hoverOut}>Register</button>
    </Link>
</div>

<style>
    h1,h2 {
        font-family: 'phatone', serif;
        color: #0900ff;
    }
    h1 {
        font-size: 4em;
    }
    h2 {
        font-size: 3em; 
        margin-top:3em;
    }
    h3 {
        font-family: 'VT323', serif;
        font-size: 2em;
        color: #0900ff;
    }
    #intro {
        font-family: 'vt323', serif;
        font-size: 1.5em;
        color: #ffffff;
        display:flex;
        place-items: center;
        word-wrap: break-word;
        padding-left: 8em;
        padding-right: 8em;
    }
    #buttons{
        margin-top: 2em;
        display: flex;
        align-items: center;
        justify-content:space-evenly;
        width:50%;
        margin-left:25%
    }

</style>