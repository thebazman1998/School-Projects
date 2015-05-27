//Basil Pocklington

import java.awt.*; 
import java.awt.event.*;
import java.util.ArrayList;
import java.util.Collections;

import javax.swing.*;

public class studentMarks extends JFrame implements ActionListener {
	
	private static final long serialVersionUID = 1L;
	
	//Declare ArrayList to store marks
	ArrayList <Integer> marks = new ArrayList<Integer>();
	
	//Create objects for labels and text fields, in the order they appear
	JLabel titleLabel = new JLabel( "Marks Program" );
	JLabel inLabel = new JLabel( "     Student Mark" );
	
	JTextField inText = new JTextField(5);
	
	JButton add = new JButton( "Add" );
	
	TextArea markLog = new TextArea( 10, 20 );
	TextArea log = new TextArea( 10, 20 );
	
	JButton sort = new JButton( "Sort" );
	JTextField fill = new JTextField( 5 );
	JButton analyze = new JButton( "Analyze" );
	
	//Define variables for stats
	int mean;
	int median;
	int mode;
	int maxMark;
	int minMark;
	int rangeMark;
	int LR;
	int L1;
	int L2;
	int L3;
	int L4;
	
	/******************************************************************************/
  	
   	//Constructor
	public studentMarks( String title ) {
		
		super( title );
      	
      	setLayout( new FlowLayout() );
      	setDefaultCloseOperation( JFrame.EXIT_ON_CLOSE ); 
      	
      	//Add elements to frame
      	add( titleLabel );
      	add( inLabel );
      	add( inText );
      	add( add );
      	add( markLog );
      	add( log );
      	add( sort );
      	add( fill );
      	add( analyze );
      	
      	//Adjust font size
      	titleLabel.setFont( titleLabel.getFont().deriveFont( 50.0f ) );
      	
      	//Set some text boxes to be un-editable
      	markLog.setEditable( false );
      	log.setEditable( false );
      	fill.setEditable( false );
      	
      	//Have buttons be their own actionListeners
      	add.addActionListener( this );
      	sort.addActionListener( this );
      	analyze.addActionListener( this );
      	
      	repaint();
	}

	/******************************************************************************/
  	
   	//Reprint the text of the log on the left
	public void update() {
		markLog.setText("");
		
		for(int i: marks) {
			markLog.setText(markLog.getText() + "\n" + i);
		}
	}
	/******************************************************************************/
  	
   	//Handle actions
	@Override
	public void actionPerformed( ActionEvent evt ) {
		
		JButton pressed = ( JButton ) evt.getSource();
		
		if( pressed.equals( add ) ) {
			int num = Integer.parseInt( inText.getText() );
			if( ( 0 <= num ) && ( num <= 100 ) )
				marks.add( num );
			inText.setText( "" );
			update();
			repaint();
		}
		else if( pressed.equals( sort ) ) {
			Collections.sort( marks );
			inText.setText( "" );
			update();
			repaint();
		}
		else if( pressed.equals( analyze ) ) {
			analyze();
			
			log.setText
			(
				"Class average: " + mean + "\n"
				+ "Class median: " + median + "\n"
				+ "Maximum mark: " + maxMark + "\n"
				+ "Minimum mark: " + minMark + "\n"
				+ "Range of marks: " + rangeMark + "\n"
				+ "Number at Level 4: " + L4 + "\n"
				+ "Number at Level 3: " + L3 + "\n"
				+ "Number at Level 2: " + L2 + "\n"
				+ "Number at Level 1: " + L1 + "\n"
				+ "Number at Level R: " + LR
			);
		}
	}
	
	/******************************************************************************/
  	
   	//Analyze marks
	public void analyze() {
		
		//Reset stats
		maxMark = minMark = marks.get(0);
		L4 = L3 = L2 = L1 = LR = mean = 0;
		
		//Cycle through marks
		for(int i: marks) 
		{
			//Add mark to mean
			mean += i;
			
			//Identify if mark is highest or lowest, or neither
			if( i > maxMark )
				maxMark = i;
			else if( i < minMark )
				minMark = i;
			
			//Keep track of the alphabetical level of each mark
			if(i < 50) LR++;
			else if( i < 60 ) L1++;
			else if( i < 70 ) L2++;
			else if( i < 80 ) L3++;
			else L4++;
		}
		
		//Calculate mean, median and range
		mean /= marks.size();
		median = marks.get(marks.size()/2);
		rangeMark = maxMark - minMark;
	}
	
	/******************************************************************************/
  	
   	//Main Method
	public static void main(String[] args) {
		
		studentMarks marks  = new studentMarks( "Student Marks" );
	    
   		marks.setSize( 400, 400 );
    	marks.setVisible( true );
	}
}
