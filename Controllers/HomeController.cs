using eigenthread.Models;
using Microsoft.AspNetCore.Mvc;
using System.Diagnostics;

namespace eigenthread.Controllers
{
    public class HomeController : Controller
    {
        private readonly ILogger<HomeController> _logger;

        public HomeController(ILogger<HomeController> logger)
        {
            _logger = logger;
        }

        public IActionResult Index()
        {
            return View();
        }

        /* button for e-Books */
        public IActionResult EBooks()
        {
            return View();
        }

        /* button for Webcrawlers */
        public IActionResult Webcrawlers()
        {
            return View();
        }

        /* button for DailyBlog */
        public IActionResult DailyBlog()
        {
            return View();
        }

        public IActionResult Agreement()
        {
            return View();
        }

        [ResponseCache(Duration = 0, Location = ResponseCacheLocation.None, NoStore = true)]
        public IActionResult Error()
        {
            return View(new ErrorViewModel { RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier });
        }
    }
}
