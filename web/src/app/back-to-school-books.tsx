"use client";

import React from "react";
import {
  Button,
  Typography,
  Tabs,
  TabsHeader,
  Tab,
} from "@material-tailwind/react";
import BookCard from "@/components/book-card";

const BOOKS = [
  {
    img: `/image/books/RectangleBig1.svg`,
    category: "Natasha Wing",
    title: "The Night Before Kindergarten",
    desc: "Um livro ilustrado bem-humorado e comovente que alivia o nervosismo do início do jardim de infância.",
    price: "$99",
    offPrice: "$79",
  },
  {
    img: `/image/books/RectangleBig6.svg`,
    category: "James Patterson",
    title: "Middle School: The Worst Years of My Life",
    desc: "Um romance divertido e compreensível sobre os desafios do ensino médio.",
    price: "$99",
    offPrice: "$79",
  },
  {
    img: `/image/books/RectangleBig2.svg`,
    category: "Helen W. Colby",
    title: "College Student: A Comprehensive Checklist",
    desc: "Um guia prático que ajuda os estudantes universitários a se prepararem para a transição para a universidade.",
    price: "$99",
    offPrice: "$79",
  },
  {
    img: `/image/books/RectangleBig3.svg`,
    category: "Walter Pauk",
    title: "How to Study in College",
    desc: "Um recurso valioso para alunos do último ano do ensino médio e calouros da faculdade, que oferece estratégias de estudo eficazes.",
    price: "$99",
    offPrice: "$79",
  },
  {
    img: `/image/books/RectangleBig4.svg`,
    category: "William Strunk Jr.",
    title: "The Elements of Style",
    desc: "Um livro de referência clássico sobre gramática e habilidades de escrita, essencial para estudantes do ensino médio e universitários.",
    price: "$99",
    offPrice: "$79",
  },
  {
    img: `/image/books/RectangleBig5.svg`,
    category: "William Strunk Jr.",
    title: "The Elements of Style",
    desc: "Um livro de referência clássico sobre gramática e habilidades de escrita, essencial para estudantes do ensino médio e universitários.",
    price: "$99",
    offPrice: "$79",
  },
];

const BOOKS_TABS = [
  "história",
  "legislação",
  "matemática",
  "economia",
  "negócios",
  "comunicação",
];

export function BackToSchoolBooks() {
  const [activeTab, setActiveTab] = React.useState("history");

  return (
    <section className="px-8 pt-20 pb-10">
      <div className="container mx-auto mb-20 text-center">
        <Typography
          variant="paragraph"
          color="blue-gray"
          className="mb-3 font-bold uppercase"
        >
         até 40% DE DESCONTO
        </Typography>
        <Typography variant="h1" color="blue-gray" className="mb-2">
        Livros de volta às aulas        </Typography>
        <Typography
          variant="lead"
          className="mx-auto w-full px-4 !text-gray-500 lg:w-9/12"
        >
          Oferecemos uma ampla variedade de guias de estudo, materiais de preparação para testes e
          livros de referência. Não importa se você está lidando com cálculo ou mergulhando em
          Shakespeare, nós o ajudamos.
        </Typography>
        <div className="mt-20 flex items-center justify-center">
          <Tabs value={activeTab} className="w-full lg:w-8/12">
            <TabsHeader
              className="h-12 bg-transparent"
              indicatorProps={{
                className: "!bg-gray-900 rounded-lg",
              }}
            >
              {BOOKS_TABS.map((book) => (
                <Tab
                  key={book}
                  value={book}
                  className={`!font-medium capitalize transition-all duration-300
                    ${activeTab === book ? "text-white" : "capitalize"}
                  `}
                  onClick={() => setActiveTab(book)}
                >
                  {book}
                </Tab>
              ))}
            </TabsHeader>
          </Tabs>
        </div>
      </div>
      <div className="container mx-auto grid grid-cols-1 items-start gap-x-6 gap-y-20 md:grid-cols-2 xl:grid-cols-3">
        {BOOKS.map((props, key) => (
          <BookCard key={key} {...props} />
        ))}
      </div>
      <div className="grid place-items-center">
        <Button className="mt-32" variant="outlined">
        Mostrar mais        </Button>
      </div>
    </section>
  );
}


export default BackToSchoolBooks;