"use client"
import React from "react";
import { lazy, Suspense, useEffect, useState } from "react";

const ChatBot = lazy(() => import("react-chatbotify"));

interface FormData {
    nome: string;
    email: string;
    classificacao: number;
    avaliacao: string;
}


export const MyChatBot = () => {
    const [isLoaded, setIsLoaded] = useState(false);
    const [form, setForm] = React.useState({});

    useEffect(() => {setIsLoaded(true);}, [])


    // Chatbot Theming
    const options = {
        isOpen: false,
        audio: {disabled: false,},
        chatHistory: {storageKey: "example_basic_form"},
        theme: {
            primaryColor: '#A9A9A9',
            secondaryColor: '#000000',
            fontFamily: 'Arial, sans-serif',
            },
        
    };
  
  
    // flow
    const flow = {
        start: {
            message: "Olá! Seja bem-vindo, em posso ser útil?",
            options: ["Suporte", "Feedback"],
            chatDisabled: true,
            path: (params) => `${params.userInput}`
        },
        Suporte: {
            message: "Descreva um pouco sobre o seu problema:",
            path: "end"
        },
        Feedback: {
            message: "Qual é o seu nome",
            function: (params) => setForm({...form, name: params.userInput}),
            path: "AskEmail"    
        },
        AskEmail:{
            message: "Qual é o seu email?",
            function: (params) => setForm({...form, email: params.userInput}),
            path: "AskClassificacao"
        },
        AskClassificacao:{
            message: "Qual é a classifcação de 1 à 5",
            checkboxes: {items: ["5", "4", "3", "2", "1"], min: 1},
            chatDisabled: true,
            function: (params) => setForm({...form, classificacao: params.userInput}),
            path:"AskAvaliacao"
        },
        AskAvaliacao: {
            message: "Digite a sua avaliação",
            function: (params) => setForm({...form, avaliacao: params.userInput}),
            path: "GotoBeginning"
        },
        GotoBeginning: {
            message: async (params) => {
				let data = await feedbackAPI(params);
                return data.title
			},
            options: ["Suporte", "Feedback"],
            chatDisabled: true,
            path: (params) => `${params.userInput}`
        },
        end: {
            message: "Muito obrigado por nos ajudar a melhorar nossos produtos e serviços",
            chatDisabled: true
        }
    }

    // Call feedback API
    const feedbackAPI = async () => {
        try {
            const response = await fetch('https://jsonplaceholder.typicode.com/todos/1', {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json',
                },
            });
            
            if(response.ok) {
                let data = await response.json();
                console.table(data);
                return data;
            }
            
        } catch (error) {
            console.error('Error:', error);
        }
    }

	return (
        <>
        {isLoaded && (
        <Suspense fallback={<div>Loading...</div>}>
             <ChatBot options={options} flow={flow} />
        </Suspense>
        )}
        </>
	);
};
