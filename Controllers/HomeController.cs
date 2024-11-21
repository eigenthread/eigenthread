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

        /* remove EBooks and consolidate to Products */
        public IActionResult EBooks()
        {
            return View();
        }

        /* remove Webcrawlers and consolidate to Products */
        public IActionResult Webcrawlers()
        {
            return View();
        }

        public IActionResult PrivacyTerms()
        {
            return View();
        }

        public IActionResult LegalTerms()
        {
            return View();
        }

        /* remove Patents and consolidate to Products */
        public IActionResult Patents()
        {
            return View();
        }
        public IActionResult Products()
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
