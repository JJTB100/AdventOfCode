import java.io.IOException;
import java.io.InputStream;
import java.util.Scanner;
import java.io.PrintStream;

public class IntCode {
    private int[] intCode;
    private int[] backupCode;
    private InputStream input;
    private PrintStream output;
    public int length;

    public IntCode(String filePath, InputStream input, PrintStream output) {
        this.input = input;
        this.output = output;
        try {
            ReadIntCode(filePath);
        } catch (IOException e) {
            System.out.println("Bad Input Pathname; File not Found." + e);
        }
        this.length = intCode.length;
        this.makeBackup();
    }

    public IntCode(String filePath) {
        try {
            ReadIntCode(filePath);
        } catch (IOException e) {
            System.out.println("Bad Input Pathname; File not Found." + e);
        }
        this.input = System.in;
        this.output = System.out;
        this.length = intCode.length;
        this.makeBackup();

    }

    public IntCode(String filePath, InputStream input) {
        try {
            ReadIntCode(filePath);
        } catch (IOException e) {
            System.out.println("Bad Input Pathname; File not Found." + e);
        }
        this.input = input;
        this.output = System.out;
        this.length = intCode.length;
        this.makeBackup();

    }

    public IntCode(String filePath, PrintStream output) {
        try {
            ReadIntCode(filePath);
        } catch (IOException e) {
            System.out.println("Bad Input Pathname; File not Found." + e);
        }
        this.input = System.in;
        this.output = output;
        this.length = intCode.length;
        this.makeBackup();

    }

    private IntCode(int[] arrayInit, InputStream input, PrintStream output) {
        this.input = input;
        this.output = output;
        this.intCode = arrayInit;
        this.length = intCode.length;
        this.makeBackup();
    }

    public IntCode clone() {
        IntCode newCode = new IntCode(intCode, input, output);
        return newCode;
    }

    public void Execute() throws Exception {
        readLoop: for (int instructionPointer = 0; instructionPointer <= intCode.length;) {
            int opCode = intCode[instructionPointer] % 100;
            int paramMode1 = (intCode[instructionPointer] % 1000 - opCode) / 100;
            int paramMode2 = (intCode[instructionPointer] % 10000 - intCode[instructionPointer] % 1000) / 1000;
            int paramMode3 = (intCode[instructionPointer] % 100000 - intCode[instructionPointer] % 10000) / 10000;
            int param1;
            int param2;
            int param3;
            
            // Do stuff
            switch (opCode) {
                case 1:
                    if (paramMode1 == 0) {
                        param1 = intCode[intCode[instructionPointer + 1]];
                    } else {
                        param1 = intCode[instructionPointer + 1];
                    }
                    if (paramMode2 == 0) {
                        param2 = intCode[intCode[instructionPointer + 2]];
                    } else {
                        param2 = intCode[instructionPointer + 2];
                    }
                    if (paramMode3 == 0) {
                        param3 = intCode[instructionPointer + 3];
                    } else {
                        param3 = instructionPointer + 3;
                    }
                    // Add - 3 params
                    intCode[param3] = param1 + param2;
                    instructionPointer += 4;
                    break;

                case 2:
                    if (paramMode1 == 0) {
                        param1 = intCode[intCode[instructionPointer + 1]];
                    } else {
                        param1 = intCode[instructionPointer + 1];
                    }
                    if (paramMode2 == 0) {
                        param2 = intCode[intCode[instructionPointer + 2]];
                    } else {
                        param2 = intCode[instructionPointer + 2];
                    }
                    if (paramMode3 == 0) {
                        param3 = intCode[instructionPointer + 3];
                    } else {
                        param3 = instructionPointer + 3;
                    }
                    // Mulitply - 3 params
                    intCode[param3] = param1 * param2;
                    instructionPointer += 4;

                    break;

                case 3:
                    if (paramMode1 == 0) {
                        param1 = intCode[intCode[instructionPointer + 1]];
                    } else {
                        param1 = intCode[instructionPointer + 1];
                    }
                    // Input - 1 param
                    Scanner scanIn = new Scanner(input);
                    output.print("Waiting on intput: ");
                    int in = scanIn.nextInt();
                    intCode[param1] = in;
                    instructionPointer += 2;

                case 4:
                    if (paramMode1 == 0) {
                        param1 = intCode[intCode[instructionPointer + 1]];
                    } else {
                        param1 = intCode[instructionPointer + 1];
                    }
                    // Output - 1 param
                    int out = intCode[param1];
                    output.println(out);
                    instructionPointer += 2;
                
                case 99:
                    // Halt - 0 params
                    break readLoop;
                default:
                    System.out.println("~~UNKNOWN OPCODE SOMETHING'S WRONG!!~~");
                    break readLoop;
            }
        }
    }

    public void ReadIntCode(String relativeFilepath) throws IOException {
        String data = FileUtil.Read(relativeFilepath);
        String[] parsedData = data.split(",");
        intCode = new int[parsedData.length];
        int i = 0;
        for (String value : parsedData) {
            intCode[i] = Integer.parseInt(value);
            i++;
        }
    }

    public int get(int index) {
        return intCode[index];
    }

    public void set(int index, int value) {
        intCode[index] = value;
    }

    public void makeBackup() {
        backupCode = intCode.clone();
    }

    public void restoreBackup() {
        intCode = backupCode.clone();
    }
}