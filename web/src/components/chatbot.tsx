const MyComponent = () => {
    const flow = {
      start: {
        message: "What is your age?",
        path: "end"
      },
      end: {
        message: (params) => `I see you are ${params.userInput}!`,
        chatDisabled: true
      }
    }
  
    return (
      <ChatBot options={{theme: {embedded: true}, chatHistory: {storageKey: "conversations_summary"}}} flow={flow}/>
    );
  };
  