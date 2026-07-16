package client;

import java.io.*;
import java.net.Socket;
import java.util.Scanner;


public class ChatClient {


    private static final String SERVER_IP =
            "localhost";

    private static final int PORT =
            5000;


    public static void main(String[] args) {


        try {


            Socket socket =
                    new Socket(
                            SERVER_IP,
                            PORT
                    );


            System.out.println(
                    "Connected to Chat Server"
            );


            BufferedReader input =
                    new BufferedReader(
                            new InputStreamReader(
                                    socket.getInputStream()
                            )
                    );


            PrintWriter output =
                    new PrintWriter(
                            socket.getOutputStream(),
                            true
                    );


            Scanner scanner =
                    new Scanner(System.in);



            // Thread to receive messages

            Thread receiver =
                    new Thread(() -> {


                try {


                    String message;


                    while(
                            (message=input.readLine())
                                    != null
                    ){


                        System.out.println(
                                message
                        );

                    }


                }
                catch(IOException e){


                    System.out.println(
                            "Disconnected from server"
                    );

                }


            });



            receiver.start();



            // Send messages

            while(true){


                String message =
                        scanner.nextLine();



                output.println(
                        message
                );



                if(message.equalsIgnoreCase("/quit")){


                    break;

                }

            }



            socket.close();

            scanner.close();


        }
        catch(IOException e){


            System.out.println(
                    "Unable to connect to server"
            );


        }


    }


}