package cs3337;

import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Random;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/Client")
public class Client extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		ArrayList<Plant> plants = (ArrayList<Plant>) getServletContext().getAttribute("plants");
		Random r = new Random();
		int x = r.nextInt(plants.size() );
		response.setContentType("text/html");
		PrintWriter out = response.getWriter();
		
		out.println("<!DOCTYPE html>");		
		out.println("<html lang=\"en\">");
		out.println("<head>");
		out.println("    <meta charset=\"UTF-8\">");
		out.println("        <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">");
		out.println("        <meta http-equiv=\"X-UA-Compatible\" content=\"ie=edge\">");
		out.println("        <link rel=\"stylesheet\" href=\"https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css\" integrity=\"sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm\" crossorigin=\"anonymous\">");
		out.println("        <title>Client</title>");
		out.println("</head>");
		out.println("<body>");
		out.println("<div class=\"container\">");
		
		out.println("<h1>" + plants.get(x).getName() + "</h1>");
		out.println("<h5>" + plants.get(x).getTemp() + "</h5>");
		out.println("<a href=\"Admin\">Admin</a>");

		out.println("</div>");
		out.println("</body>");
		out.println("</html>");
}

	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		doGet(request, response);
	}

}