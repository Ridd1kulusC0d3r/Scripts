       IDENTIFICATION DIVISION.
       PROGRAM-ID. HelloWorld.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 MESSAGE-TEXT PIC X(20) VALUE 'Olá, Mundo!'.
       PROCEDURE DIVISION.
           DISPLAY MESSAGE-TEXT.
           STOP RUN.
