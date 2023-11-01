<!-- Svelte component representing the Signup page -->
<script>
    // Imports
    import {signupUser} from "./store.js"
    import {Link} from "svelte-routing";
    let signupError = null

    /**
     * Event handler for the form submit event, makes an api call to the signup api using
     * the information given in the form inputs.
     * @param event The event caller
    */
    async function handleForm(event){
        event.preventDefault();
        // console.log($user)
        try{
            // Make a POST request to the signup api by passing the user object in the store
            const reponse = await fetch('http://127.0.0.1:8000/api/signup', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify($signupUser),
            });
            
            if(reponse.ok) {
                signupError= null;
                console.log('Sign up succesful');
                window.location.href='/login';
            } else {
                const error = await reponse.json();
                console.error(error)
                signupError = error[0]
                if(error.error === "Passwords do not match"){
                    signupError = error.error;
                }

                if(signupError === 'UNIQUE constraint failed: auth_user.username'){
                    signupError = 'Email has already been taken. Please log in if you already have an account'
                }
                console.log(signupError)
            }
        } catch(error){
            console.error(error);
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
<h4>Sign up and make friends</h4>
{#if signupError}
    <div class="error-message">{signupError}</div>
{/if}

<!-- Form for signup information -->
<form on:submit={handleForm}>
    <div id="flexBox">
        <div class="idky">
            <lable for="email">Email: </lable>
            <input bind:value={$signupUser.email} type="text" id="email" name="email" style="input_item">
        </div>
        <div class="idky">
            <lable for="pw">Password: </lable>
            <input bind:value={$signupUser.password} type="password" id="pw" name="pw">
        </div>
        <div class="idky">
            <lable for="cpw">Confirm Password: </lable>
            <input bind:value={$signupUser.confirmPw} type="password" id="cpw" name="cpw">
        </div>
    </div>
    <!-- svelte-ignore a11y-mouse-events-have-key-events -->
    <input type="submit" id="button" value="Sign Up" on:mouseenter={hoverOver} on:mouseout={hoverOut}>
    <p>Already have an account? Click <Link to="/login"> here </Link> to log in!</p>
</form>

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

    #button{
        width:8em;
        font-size:1.2em;
        padding-left:0em;
        margin-top:1em;
        align-items: center;
        border-color:#0900ff;

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
    }

    .error-message{
        font-family: "VT323";
        font-size:2em;
        color:red;

    }


</style>