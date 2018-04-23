package cs3337;

import java.io.IOException;
import java.util.ArrayList;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/DeletePlant")
public class DeletePlant extends HttpServlet {
	private static final long serialVersionUID = 1L;

	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		ArrayList<Plant> plants = (ArrayList<Plant>) getServletContext().getAttribute("plants");
		int id = Integer.parseInt(request.getParameter("id"));
		for (Plant p : plants) {
			if (p.getId() == id) {
				plants.remove(p);
				break;
			}
		}
		response.sendRedirect("Admin");
	}

	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		doGet(request, response);
	}

}