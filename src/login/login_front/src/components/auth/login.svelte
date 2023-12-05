<script>
//  Imports
    import {username, password, csrf, handleCsrf, userid} from "../store.js"
    import {Link, navigate} from 'svelte-routing';
    // let loginError = null
    
    /**
     * Event handler for the form submit event, makes an api call to the login api using
     * the information given in the form inputs.
     * @param event The event caller
    */
    function handleEnterPressed(event) {
        if ((event.key) === 'Enter') {
            handleLogin();
        }
    }

    async function handleLogin(event) {
        await handleCsrf()
        console.log($csrf)
        console.log('csrftoken:', $csrf)
        // This is to fix an issue where CSRF cookie not set (basically csrf token is different between the one returned from Django server and the one in browser cookie)
        // document.cookie = 'csrftoken=' + $csrf;
        let res = await fetch("http://localhost:8000/login/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": $csrf,
            },
            credentials: "include",
            body: JSON.stringify({username: $username, password: $password}),
        })

        let dat = await res.json()

        userid.set(dat.userid)
        console.log($userid)
        
        if (res.ok) {
            navigate('/chat')
        }        
        
    }

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
<Link to="/">
    <h1>ByteBuddy</h1>
</Link>
<h4>Log into your community</h4>
    <div id="flexBox">
        <div class="idky">
            <lable for="email">Email: </lable>
            <input bind:value={$username} type="text" on:keypress={handleEnterPressed}>
        </div>
        <div class="idky">
            <lable for="pw">Password: </lable>
            <input bind:value={$password} type="password" on:keypress={handleEnterPressed}>
        </div>
    </div>
    <!-- svelte-ignore a11y-mouse-events-have-key-events -->
    <button on:click={handleLogin} on:mouseenter={hoverOver} on:mouseout={hoverOut}>Login</button>
    <p>Haven't registered an account? Click <Link to="/signup"> here </Link> to sign up!</p>

<style>
    #flexBox{
        display: flex;
        flex-direction: column;
        justify-content: space-evenly;
        align-items: center;
        font-family: "VT323", serif;
        font-size: 1.5em;
        height: 6em;
    }
    lable{
        width:5em;
        color:white;
        text-align: right;
    }

    .idky{
        display:flex;
        flex-direction: row;
        justify-content: space-evenly;
        width:20em;
    }
    input{
        width:10em;
        border-radius: 0.5em;
        color:white;
        background-color: #0900ff;
        border-color: white;
        padding-left: 1em;
        height:2em;
        font-family: "VT323", serif;
    }

    button{
        border-color: white;
        color: white;
    }

    h1,h2 {
        font-family: 'phatone', serif;
        color: #0900ff;
        /* max-width: 50vw; */
    }

    h4 {
        font-family: 'VT323', serif;
        font-size: 2em;
        color: #0900ff;
        margin-bottom:0;
    }

    h1 {
        font-size: 4em;
    }

    h2 {
        font-size: 3em;
        margin-top:4em;
    }

    /* .error-message{
        font-family: "VT323";
        font-size:2em;
        color:red;

    } */

</style>