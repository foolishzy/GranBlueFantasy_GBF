import javax.swing.JOptionPane;

public class Alert {

    public Alert() {
    }

    public void run() {
        sound();
        endBox("finished", "finished" , "ok"  );
    }

    public void sound() {
        System.out.println("/a");
    }

    public void endBox(String msg, String title, String bt) {
        JOptionPane.showMessageDialog(null, msg, title, JOptionPane.INFORMATION_MESSAGE);
    }

    public static void main(String[] args) {
        Alert alert = new Alert();
        alert.run();
    }
}

