package main

import (
	"fmt"
	"time"
	"isa-layer0-router/pkg/synchronization"
)

func main() {
	fmt.Println("ISA Layer-0 Daemon Initializing...")
	orch := synchronization.NewRouterOrchestrator(100 * time.Millisecond)
	err := orch.RegisterCloudTarget("primary-edge-01", "azure-us-east")
	if err != nil {
		panic(err)
	}
	fmt.Println("Dynamic state routing matrix successfully established.")
}
