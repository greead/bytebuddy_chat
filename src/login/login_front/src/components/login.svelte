<script>
//  Imports
    import {user} from "./store.js"

    /**
     * Event handler for the form submit event, makes an api call to the login api using
     * the information given in the form inputs.
     * @param event The event caller
    */
    async function handleForm(event){
        event.preventDefault();
        // console.log($user)
        try{
            // Make a POST request to the signup api by passing the user object in the store
            const reponse = await fetch('http://127.0.0.1:8000/api/login', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify($user),
            });
            
            if(reponse.ok) {
                console.log('Log in succesfully');
            } else {
                const error = await reponse.json();
                console.error(error.message);
            }
        } catch(error){
            console.error(error);
        }
    }

    async function signOut(event){
        event.preventDefault;
        try{
            const response = await fetch('http://127.0.0.1:8000/api/logout', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
            });
            if(response.ok) {
                console.log('Log out succesfully');
            } else {
                const error = await response.json();
                console.error(error.message);
            }
        } catch(error){
            console.error(error);
        }
    }
</script>

<h1>ByteBuddy Signup</h1>

<!-- Form for signup information -->
<form on:submit={handleForm}>
    <lable for="email">Email: </lable>
    <input bind:value={$user.email} type="text" id="email" name="email" style="input_item"><br>
    <lable for="pw">Password: </lable>
    <input bind:value={$user.password} type="password" id="pw" name="pw"><br>
    <input type="submit" id="button" value="Log in">
</form>

<button on:click={signOut}>log out</button>
<style>
    form{
        display: flex;
        flex-direction: column;
        align-items: center;
    }

    input{
        width:20em;
        
    }

    #button{
        width:10em;
    }

</style>