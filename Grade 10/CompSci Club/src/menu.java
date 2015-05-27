import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JPanel;


public class menu extends JPanel {
	public menu(){
		
		setSize(300, 200);
		this.setLayout(null);
		
		JButton start1p = new JButton("Start Survival");
		//x, y, width, height
		start1p.setBounds(20, 20, 180, 50);
		start1p.addActionListener( new ActionListener()
		{
			public void actionPerformed(ActionEvent e)
			{
				String[] args = {"asdf","asdf"};
				new Game().main(args);
				System.out.println("SP_Start");
			}
		});
		add(start1p);

	}
	
	public static void main(String[] args) {

		JFrame f = new JFrame();
		menu m = new menu();
		f.setTitle("Left 2 Die");
		f.setResizable(false);
		f.setSize(1000, 600);
		f.setLocationRelativeTo(null);
		f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		f.add(m);
		m.repaint();
		f.setVisible(true);


	}
}