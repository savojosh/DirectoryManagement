/*
Java Edition
*/

//----- IMPORTS -----\\

import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.math.BigInteger;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;

//----- CLASS -----\\
/**
 * <h3>FileComparison</h3>
 * 
 * Compares all files in a directory to check for duplicates based on the byte content of the files.
 */
public class FileComparison {
    
    private static MessageDigest messageDigest;

    // On compilation, check to see if the SHA-512 hash function exists.
    static {
        try {
            messageDigest = MessageDigest.getInstance("SHA-512");
        } catch (NoSuchAlgorithmException e) {
            throw new RuntimeException("Cannot initialize SHA-512 hash function", e);
        }
    }

    public static void findDuplicates(Map<String, List<String>> lists, File dir) {
        for(File f : dir.listFiles()) {
            if(f.isDirectory()) {
                findDuplicates(lists, f);
            } else {
                try {
                    FileInputStream fi = new FileInputStream(f);
                    byte fileData[] = new byte[(int) f.length()];

                    fi.read(fileData);
                    fi.close();

                    String hash = new BigInteger(1, messageDigest.digest(fileData)).toString(16);
                    List<String> list = lists.get(hash);

                    if(list == null) {
                        list= new LinkedList<String>();
                    }

                    list.add(f.getAbsolutePath());

                    lists.put(hash, list);
                } catch(IOException e) {
                    throw new RuntimeException("Cannot read file " + f.getAbsolutePath(), e);
                }
            }
        }
    }

}
