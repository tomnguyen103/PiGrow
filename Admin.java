package cs3337;

import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;

import javax.servlet.ServletConfig;
import javax.servlet.ServletContext;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/Admin")
public class Admin extends HttpServlet {
	private static final long serialVersionUID = 1L;

	public void init(ServletConfig config) throws ServletException {
		super.init(config);
		ArrayList<Plant> plants = new ArrayList<Plant>();
		plants.add(new Plant("Eggplant", 75));
		plants.add(new Plant("Corn", 55));
		plants.add(new Plant("Peppers", 65));
		plants.add(new Plant("Beans", 72));
		plants.add(new Plant("Carrots", 45));
		plants.add(new Plant("Turnip", 50));
		plants.add(new Plant("Cantaloupe", 68));
		plants.add(new Plant("Squash", 70));
		getServletContext().setAttribute("plants", plants);
	}

	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		response.setContentType("text/html");
		PrintWriter out = response.getWriter();
		out.println("<!DOCTYPE html>");
		out.println("<html lang=\"en\">");
		out.println("<head>");
		out.println("    <meta charset=\"UTF-8\">");
		out.println("        <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">");
		out.println("        <meta http-equiv=\"X-UA-Compatible\" content=\"ie=edge\">");
		out.println("        <link rel=\"stylesheet\" href=\"https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css\" integrity=\"sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm\" crossorigin=\"anonymous\">");
		out.println("        <title>Admin</title>");
		out.println("</head>");
		out.println("<body>");
		out.println("<div class=\"container\">");
		out.println("<h1>Plant List</h1>");
		ServletContext context = getServletContext();
		ArrayList<Plant> plants = (ArrayList<Plant>) context.getAttribute("plants");

		out.println("<table class=\"table table-bordered table-striped table-hover\">");
		out.println("<tr><td>Plant Name</td>");
		out.println("<td>Temp</td>");
		out.println("<td>Water?:</td>");
		out.println("<td>Fan?:</td>");
		out.println("<td>Light?:</td>");
		out.println("<td>Delete Plant?:</td>");
		out.println("<td>Update Live Feed?:</td></tr>");

		for (Plant p: plants) {
			out.println("<tr>");
			out.println("<td>" + p.getName() + "</td>");
			out.println("<td>" + p.getTemp() + "</td>");
			out.println("<td><a class=\"btn btn-primary\" href=\"Water?id=" + p.getId() + "\">Water</a></td>");
			out.println("<td><a class=\"btn btn-primary\" href=\"Fan?id=" + p.getId() + "\">Fan</a></td>");
			out.println("<td><a class=\"btn btn-primary\" href=\"Light?id=" + p.getId() + "\">Light</a></td>");
			out.println("<td><a class=\"btn btn-primary\" href=\"DeletePlant?id=" + p.getId() + "\">Delete</a></td>");
			out.println("<td><a class=\"btn btn-primary\" href=\"Update?id=" + p.getId() + "\">Update</a></td>");
			out.println("</tr>");
		}
		out.println("</table>");
		out.println("<a href=\"Client\" class=\"btn btn-primary\">Client</a>");

		out.println("</div>");
		out.println("</body>");
		out.println("</html>");
	}

	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		doGet(request, response);
	}

}
