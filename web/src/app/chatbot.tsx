"use client"
import React from "react";
import { lazy, Suspense, useEffect, useState } from "react";

const ChatBot = lazy(() => import("react-chatbotify"));

interface FormData {
    nome_cliente: string;
    email: string;
    classificacao: number;
    descricao: string;
    canal_feedback: string;
    produto: string;
}

const initialState: FormData = {
    nome_cliente: "Juclénio António",
    email: "juclenio@example.com",
    classificacao: 5,
    descricao: "lorem ipsum dolor sit amet, consectetur adipiscing elit.",
    canal_feedback: "EMAIL",
    produto: "PRODUTOA",

}


export const MyChatBot = () => {
    const [isLoaded, setIsLoaded] = useState(false);
    // const [form, setForm] = React.useState({});
    const [formData, setFormData] = useState<FormData>(initialState);

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
            // path: (params) => {
            //     switch (params.userInput) {
            //         case "Suporte":
            //             return "opcoesSuporte";
            //         case "Feedback":
            //             return "Feedback";
            //         default:
            //             return "opcoesSuporte";
            //     }
            // }
        },
        opcoesSuporte: {
            message: "Quais as opções de suporte?",
            options: ["Como funciona", "Como usar", "Outras dúvidas"],
            chatDisabled: true,
            path: (params) => {
                switch (params.userInput) {
                    case "Como funciona":
                        return "ComoFunciona";
                    case "Como usar":
                        return "ComoUsar";
                    case "Outras dúvidas":
                        return "OutrasDudas";
                    default:
                        return "end";
                }
            }
        },
        Suporte: {
            message: "Descreva um pouco sobre o seu problema",
            path: "RespostaSuporte"
        },
        RespostaSuporte:{
            message: async (params) => {
                let data = await supportAPI(params);
                return data.response.trim();
			},
            chatDisabled: true,
            transition: {duration: 1000},
            path: "SuporteOpcoes"
        },
        SuporteOpcoes:{
            message:'Tem mais alguma pergunta?"',
            options: ["Sim", "Não"],
            chatDisabled: true,
            path: (parms) => {
                switch (parms.userInput) {
                    case "Sim":
                        return "Suporte";
                    case "Não":
                        return "end";
                    default:
                        return "end";
            }},},
        Feedback: {
            message: "Qual é o seu nome",
            function: (params) => setFormData({...formData, nome_cliente: params.userInput}),
            path: "AskEmail"    
        },
        AskEmail:{
            message: "Qual é o seu email?",
            function: (params) => setFormData({...formData, email: params.userInput}),
            path: "AskClassificacao"
        },
        AskClassificacao:{
            message: "Qual é a classifcação de 1 à 5",
            checkboxes: {items: ["5", "4", "3", "2", "1"], min: 1},
            chatDisabled: true,
            function: (params) => setFormData({...formData, classificacao: params.userInput}),
            path:"AskAvaliacao"
        },
        AskAvaliacao: {
            message: "Digite a sua avaliação",
            function: (params) => setFormData({...formData, descricao: params.userInput}),
            path: "GotoBeginning"
        },
        GotoBeginning: {
            message: async (params) => {
				let data = await feedbackAPI(params);
                return data
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
            const response = await fetch('http://127.0.0.1:8000/api/feedback/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(formData),
            });
            
            if(response.ok) {
                let data = await response.json();
                console.table(data);
                return "data enviado com sucesso!";
            }else{
                let data = await response.json();
                console.table(data);
                return "Erro ao enviar dados!";
            }
            
        } catch (error) {
            console.error('Error:', error);
        }
    }

      // Call support API
      const supportAPI = async (params) => {
        try {
            const response = await fetch('http://127.0.0.1:8000/api/faq/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({query:params.userInput}),
            });
            
            if(response.ok) {
                let data = await response.json();
                console.table(data);
                return data;
            }else{
                let data = await response.json();
                console.table(data);
                return "Erro ao enviar dados!";
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
