package server;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.time.LocalDateTime;


public class ChatLogger {

    private static final String LOG_FILE =
            "logs/chat_history.log";


    public static void log(String message) {

        try {

            File file =
                    new File(LOG_FILE);


            file.getParentFile()
                    .mkdirs();


            FileWriter writer =
                    new FileWriter(file, true);


            writer.write(
                    "["
                    + LocalDateTime.now()
                    + "] "
                    + message
                    + System.lineSeparator()
            );


            writer.close();


        } catch (IOException e) {

            System.out.println(
                    "Logger Error: "
                    + e.getMessage()
            );
        }
    }
}