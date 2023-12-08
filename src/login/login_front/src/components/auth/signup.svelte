<script>
    import {username, password, handleCsrf, csrf} from "../store.js"
    import {Link, navigate} from "svelte-routing";
    let signupError = null
    let confirmPassword = '';
    $: isMatching = $password === confirmPassword
    $: isDisabled = $password == '' || $username == '' || !isMatching
    $: console.log($password)

    function handleEnterPressed(event) {
        if ((event.key) === 'Enter') {
            handleSignUp();
        }
    }

    /**
     * Event handler for the form submit event, makes an api call to the signup api using
     * the information given in the form inputs.
     * @param event The event caller
    */
    async function handleSignUp(event){
        event.preventDefault();
        signupError = null
        if($password != confirmPassword){
            signupError = "Passwords do not match"
        }
        else{
        await handleCsrf()
        // console.log('csrftoken:', $csrf)
        // Make a POST request to the signup api by passing the user object in the store
        let reponse = await fetch('http://localhost:8000/signup/', {
            method: 'POST',
            headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": $csrf,
        },
            credentials: "include",
            body: JSON.stringify({username: $username, password: $password}),
            });
          
        
        if(reponse.ok) {
            signupError= null;
            console.log('Sign up succesful');
            navigate('/')
        } else {
                const error = await reponse.json();
                signupError = error.detail
        }
    }
    }   
</script>

<h2>Welcome to</h2>
<Link to="/">
    <h1>ByteBuddy</h1>
</Link>
<h4>Sign up and make friends</h4>
{#if signupError}
    <div class="error-message">{signupError}</div>
{/if}

    <div id="flexBox">
        <div class="idky">
            <lable for="email">Email: </lable>
            <input bind:value={$username} type="email" id="email" name="email" style="input_item" on:keypress={handleEnterPressed}>
        </div>
        <div class="idky">
            <lable for="pw">Password: </lable>
            <input bind:value={$password} type="password" id="pw" name="pw" on:keypress={handleEnterPressed}>
        </div>
        <div class="idky">
            <lable for="cpw">Confirm Password: </lable>
            <input bind:value={confirmPassword} type="password" id="cpw" name="cpw" on:keypress={handleEnterPressed}>
        </div>
        
    </div>
    {#if !isMatching}
        <p class="matching">Passwords do not match.</p>
    {/if}
    <button id="button" on:click={handleSignUp} disabled={isDisabled} class:disabled={isDisabled}>Sign Up</button>
    <p>Already have an account? Click <Link to="/login"> here </Link> to log in!</p>

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

    .matching {
        color: red;
    }

    lable{
        width:7em;
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

    .disabled {
        background-color: grey;
    }

    button{
        /* width:8em; */
        /* font-size:1.2em; */
        /* padding-left:0em; */
        margin-top:1em;
        align-items: center;
        border-color: white;
        color: white;

    }

    h1,h2 {
        font-family: 'phatone', serif;
        color: #0900ff;
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

    .error-message{
        font-family: "VT323";
        font-size:2em;
        color:red;

    } 


</style>