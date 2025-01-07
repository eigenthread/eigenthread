﻿// File: /Controllers/USPTOPatentSearchController.cs
/*sing Microsoft.AspNetCore.Mvc;

namespace eigenthread.Controllers
{
    [ApiController]
    [Route("api/[controller]")] // Routes to /api/usptopatentsearch
    public class USPTOPatentSearchController : ControllerBase
    {
        [HttpGet("search")] // Routes to /api/usptopatentsearch/search
        public IActionResult Search()
        {
            return Ok(new { Message = "USPTO Patent Search API is working!" });
        }
    }
}
*/

// File: /Controllers/USPTOPatentSearchController.cs
using Microsoft.AspNetCore.Mvc;

namespace eigenthread.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class USPTOPatentSearchController : ControllerBase
    {
        [HttpGet("search")]
        public IActionResult Search()
        {
            return Ok(new { Message = "USPTO Patent Search API is working!" });
        }
    }
}
