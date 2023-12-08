import { writable, derived, get } from 'svelte/store';
/**
 * This is the Svelte shared store.
 * 
 * Within this class are several sections that each are responsible for a certain function in the Svelte ecosystem.
 * Each section is self contained but is visible to the Svelte ecosystem for interconnectedness.
 * This Svelte store takes advantage of Svelte's built-in Observer system. Observers can be noted by the use of the
 * Writable or Derived constants.
 * 
 * ****** Store responsibilities ******
 * Auth store: Authentication-related observables
 * Profile store: Profile-related observables
 * Room store: Room list-related observables
 * User store: User list-related observables
 * Chat store: Message and chat consumer websocket-related observables
 * IDE store: IDE and IDE consumer websocket-related observables
 */


// AUTH STORE //
export const csrf = writable(''); // Current CSRF token
export const username = writable(''); // Username
export const password = writable(''); // Password
export const userid = writable(localStorage.getItem("userid") || ""); // User ID
userid.subscribe(val => localStorage.setItem("userid", val));

/**
 * Handler that fetches CSRF tokens for authentication.
 * @param {*} event The event caller.
 */
export async function handleCsrf(event) {
  let res = await fetch("http://localhost:8000/csrf/", {
      credentials: "include",
  })

  csrf.set(res.headers.get("X-CSRFToken"))
}
// AUTH STORE //

// PROFILE STORE //
export const displayName = writable('') // User display name
export const bio= writable('') // User bio
export const img= writable('') // User profile picture
// PROFILE STORE //

// ROOM STORE //
export const current_room = writable('') // Currently connected room
// ROOM STORE //

// USER STORE //
export const user_store = writable([]) // List of currently active users
// USER STORE //

// CHAT STORE //
export const uri = writable('') // Current chat websocket URL
export const message_list = writable([]) // Current message list

/**
 * Complex Svelte store that allows the system to create a websocket system that does not
 * connect to any websockets before the user chooses to do so.
 * @param url The URL for the websocket to connect to.
 * @returns A WebSocket store.
 */
function createWebSocketStore(url) {
  const { subscribe, set, update } = writable({
    websocket: null,
    message: '',
    isConnected: false,
  });

  let ws;

  /**
   * Store function to initiate websocket connection
   */
  const connectWebSocket = () => {
    user_store.set([])
    ws = new WebSocket(url);

    /**
     * Websocket onOpen event
     * 
     * Updates connection status
     */
    ws.onopen = () => {
      update((state) => ({ ...state, websocket: ws, isConnected: true }));
      console.log('WebSocket opened at:', url);
    };

    /**
     * Websocket onMessage event
     * 
     * Updates different stores depending on message type and contents.
     * @param event The event contents.
     */
    ws.onmessage = (event) => {
      // update((state) => ({ ...state, message: event.data }));
      // console.log('WebSocket message received:', event.data)
      const data = JSON.parse(event.data);
      console.log(data);
      switch (data.type) {
        case "chat_message":
          message_list.update((list) => ([...list, {user:data.user, content:data.message}]))
          // update((state) => ({ ...state, message: data.user + ": " + data.message }));
          break;
        case "message_list":
          message_list.set(data.message)
          break;
        case "user_list":
          user_store.set(data.message);
          break;
        case "user_join":
          message_list.update((list) => ([...list, {user:data.user, content:data.message, sys:true}]))
          break;
        case "user_leave":
          message_list.update((list) => ([...list, {user:data.user, content:data.message, sys:true}]))
          break;     
        default:
          console.error("Unknown message type!");
          break;
      }
    };

    /**
     * Websocket onClose event
     * 
     * Updates connection status.
     */
    ws.onclose = () => {
      update((state) => ({ ...state, websocket: null, isConnected: false }));
      console.log('WebSocket closed at:', url)
    };

    /** Websocket onError event
     * 
     * Logs errors in the console.
     */
    ws.onerror = (error) => {
      console.error('WebSocket error:', error);
    };
  };

  /**
   * Store function to disconnect from the websocket
   */
  const disconnectWebSocket = () => {
    if (ws) {
      ws.close();
    }
  };

  /**
   * Store function to initiate sending a message through the websocket
   * @param msg The message contents.
   */
  const sendMessage = (msg) => {
    if(ws) {
        ws.send(JSON.stringify({
          "message":msg
        }));
        console.log('WebSocket message sent:', msg)
    }
  };

  // Store functions made visible
  return {
    subscribe,
    connectWebSocket,
    disconnectWebSocket,
    sendMessage,
  };
};

export const wss = derived(uri, ($uri) => createWebSocketStore($uri)); // Dynamic chat websocket store
// CHAT STORE //

// IDE STORE //
export const uri_ide = writable('') // Current IDE websocket URL
export const ide_contents = writable() // Latest IDE delta received
export const ide_state = writable("") // Latest IDE state received

/**
 * Complex Svelte store that allows the system to create a websocket system that does not
 * connect to any websockets before the user chooses to do so.
 * @param url The URL for the websocket to connect to.
 * @returns A WebSocket store.
 */
function createIDESocketStore(url) {
  const { subscribe, set, update } = writable({
    websocket: null,
    isConnected: false,
  });

  let ws;

  /**
   * Websocket onOpen event
   * 
   * Updates connection status
   */
  const connectWebSocket = () => {
    ws = new WebSocket(url);

    /**
     * Websocket onOpen event
     * 
     * Updates connection status
     */
    ws.onopen = () => {
      update((state) => ({ ...state, websocket: ws, isConnected: true }));
      console.log('WebSocket opened at:', url);
    };

    /**
     * Websocket onMessage event
     * 
     * Updates different stores depending on message type and contents.
     * @param event The event contents.
     */
    ws.onmessage = (event) => {
      const data = JSON.parse(event.data);
      console.log("RECEIVED", data);
      switch (data.type) {
        case "ide_message":
          if (data.user != get(username)) {
            ide_contents.set(data.message)
          }
          break;
        case "ide_connect":
          ide_state.set(data.message)
      }
    };

    /**
     * Websocket onClose event
     * 
     * Updates connection status.
     */
    ws.onclose = () => {
      update((state) => ({ ...state, websocket: null, isConnected: false }));
      console.log('WebSocket closed at:', url)
    };

    /** Websocket onError event
     * 
     * Logs errors in the console.
     */
    ws.onerror = (error) => {
      console.error('WebSocket error:', error);
    };
  };

  /**
   * Store function to disconnect from the websocket
   */
  const disconnectWebSocket = () => {
    if (ws) {
      ws.close();
    }
  };

  /**
   * Store function to initiate sending a message through the websocket
   * @param msg The message contents.
   */
  const sendMessage = async (msg) => {
    if(ws.readyState === ws.OPEN) {
        await ws.send(JSON.stringify({
          "message":msg
        }));
        console.log('WebSocket message sent:', msg)
    }
  };

  // Store functions made visible
  return {
    subscribe,
    connectWebSocket,
    disconnectWebSocket,
    sendMessage,
  };
};

export const wss_ide = derived(uri_ide, ($uri_ide) => createIDESocketStore($uri_ide)) // Dynamic IDE websocket store
// IDE STORE //
