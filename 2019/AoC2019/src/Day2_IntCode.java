public class Day2_IntCode {
    public static void main(String[] args) throws Exception {
        IntCode intCode = new IntCode("Day2.txt");
        for (int i = 0; i <= 99; i++) {
            for (int j = 0; j <= 99; j++) {
                intCode.set(1, i);
                intCode.set(2, j);
                intCode.Execute();
                if (intCode.get(0) == 19690720) {
                    System.out.println(100 * i + j);
                }
                intCode.restoreBackup();
            }
        }
    }
}
