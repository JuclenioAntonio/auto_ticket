"use client";
import "./globals.css";
import type { Metadata } from "next";
import { Roboto } from "next/font/google";
import { Layout, FixedPlugin } from "@/components";
import { lazy, Suspense, useEffect, useState } from "react";
import { MyChatBot } from "./chatbot";



// const ChatBot = lazy(() => import("react-chatbotify"));

const roboto = Roboto({
  subsets: ["latin"],
  weight: ["300", "400", "500", "700", "900"],
  display: "swap",
});

// Chatbot configuration
// -----------------------
// ----------------------

// Theming
const options = {
  isOpen: false,
  // ...other configurations
  theme: {
    primaryColor: '#A9A9A9',
    secondaryColor: '#000000',
    fontFamily: 'Arial, sans-serif',
  },
  audio: {
    disabled: false,
  },
  chatHistory: {storageKey: "example_basic_form"}
  // ...other styles
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
    path: "AskEmail"

  },
  AskEmail:{
    message: "Qual é o seu email?",
    path: "AskClassificacao"
  },
  AskClassificacao:{
    message: "Qual é a classifcação de 1 à 5",
    checkboxes: {items: ["⭐⭐⭐⭐⭐", "⭐⭐⭐⭐", "⭐⭐⭐", "⭐⭐", "⭐"], min: 1},
    chatDisabled: true,
    path:"AskAvaliacao"
  },
  AskAvaliacao: {
    message: "Digite a sua avaliação",
    path: "GotoBeginning"
  },
  GotoBeginning: {
    message: "Muito obrigado pelo teu feedback, em que mais podemos te ajudar?",
    options: ["Suporte", "Feedback"],
    chatDisabled: true,
    path: (params) => `${params.userInput}`
  },
  end: {
    message: "Muito obrigado por nos ajudar a melhorar nossos produtos e serviços",
    chatDisabled: true
  }
}

// ----------------------------------------
// ----------------------------------------


export const metadata: Metadata = {
  title: "NextJS Tailwind Campaign Page",
  description:
    "Introducing Tailwind Campaign Page, an all-inclusive and visually captivating campaign landing page template built on the foundation of Tailwind CSS and Material Tailwind.",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {

  

  const [isLoaded, setIsLoaded] = useState(false);
  useEffect(() => {
    setIsLoaded(true);
  }, [])

  return (
    <html lang="en">
      <head>
        <script
          defer
          data-site="YOUR_DOMAIN_HERE"
          src="https://api.nepcha.com/js/nepcha-analytics.js"
        ></script>
        <link rel="shortcut icon" href="/favicon.png" type="image/png" />
      </head>
      <body className={roboto.className}>
        <Layout>
        
          {children}
          {/* <FixedPlugin /> */}
          {isLoaded && (
            <Suspense fallback={<div>Loading...</div>}>
              <MyChatBot />
              {/* <ChatBot options={options} flow={flow} /> */}
            </Suspense>
          )}
        </Layout>
      </body>
    </html>
  );
}
